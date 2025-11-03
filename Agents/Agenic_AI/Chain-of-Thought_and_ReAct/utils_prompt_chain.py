#
# This is utils func for insurance claim agent example. 
#
import json
from pydantic import BaseModel, Field  # For structured data validation
from typing import List, Literal, Optional
from utils import get_completion


class ClaimInformation(BaseModel):
    claim_id: str = Field(..., min_length=2, max_length=10)
    name: str = Field(..., min_length=2, max_length=100)
    vehicle: str = Field(..., min_length=2, max_length=100)
    loss_desc: str = Field(..., min_length=10, max_length=500)
    damage_area: List[
        Literal[
            "windshield",
            "front",
            "rear",
            "side",
            "roof",
            "hood",
            "door",
            "doors",
            "bumper",
            "fender",
            "quarter panel",
            "taillight", 
            "rear bumper",
            "radiator",
            "engine compartment",
            "airbags",
            "trunk",
            "glass",
            "mirror",
            "window",
        ]
    ] = Field(..., min_items=1)


def gate1_validate_claim_info(claim_info_json: str) -> ClaimInformation:
    """
    Gate 1: Validates claim information extracted from FNOL text.
    Returns validated ClaimInformation object or raises validation error.
    """
    try:
        # Parse the JSON string
        claim_info_dict = json.loads(claim_info_json)
        # Validate with Pydantic model
        validated_info = ClaimInformation(**claim_info_dict)
        return validated_info
    except Exception as e:
        raise ValueError(f"Gate 1 validation failed: {str(e)}")


def extract_claim_info(client, fnol_text, info_extraction_system_prompt):
    """
    Stage 1: Extract structured information from FNOL text
    """
    messages = [
        {"role": "system", "content": info_extraction_system_prompt},
        {"role": "user", "content": fnol_text},
    ]

    response = get_completion(client, messages=messages)

    # Gate check: validate the extracted information
    try:
        validated_info = gate1_validate_claim_info(response) # ********** <-- Run the gate check on the response
        return validated_info
    except ValueError as e:
        print(f"Gate 1 failed: {e}, by {response}")
        return None


# ------------------------------------------------------------------------------
# Define a system prompt for severity assessment according to the provided SeverityAssessment class
class SeverityAssessment(BaseModel):
    severity: Literal["Minor", "Moderate", "Major"]
    est_cost: int = Field(..., gt=0)


# Define a gate check function and assess_severity function
def gate2_cost_range_ok(severity_json: str) -> SeverityAssessment:
    """
    Gate 2: Validates that the estimated cost is within reasonable range for the severity.
    Returns validated SeverityAssessment object or raises validation error.
    """
    try:
        # Parse the JSON string
        severity_dict = json.loads(severity_json)
        # Validate with Pydantic model
        validated_severity = SeverityAssessment(**severity_dict)

        # Check cost range based on severity
        if (
            validated_severity.severity == "Minor"
            and not (
                validated_severity.est_cost < 1000 or validated_severity.est_cost > 100
            )
        ):
            raise ValueError(
                f"Minor damage should cost between $100-$1000, got ${validated_severity.est_cost}"
            )
        elif (
            validated_severity.severity == "Moderate"
            and not (
                validated_severity.est_cost < 5000 or validated_severity.est_cost >= 1000
            )
        ):
            raise ValueError(
                f"Moderate damage should cost between $1000-$5000, got ${validated_severity.est_cost}"
            )
        elif (
            validated_severity.severity == "Major"
            and not (
                validated_severity.est_cost < 50000 or validated_severity.est_cost >= 5000
            )
        ):
            raise ValueError(
                f"Major damage should cost between $5000-$50000, got ${validated_severity.est_cost}"
            )

        return validated_severity
    except Exception as e:
        raise ValueError(f"Gate 2 validation failed: {str(e)}")


def assess_severity(client, severity_assessment_system_prompt, claim_info: ClaimInformation) -> Optional[SeverityAssessment]:
    """
    Stage 2: Assess severity based on damage description
    """

    # Convert Pydantic model to JSON string
    claim_info_json = claim_info.model_dump_json()

    messages = [
        {"role": "system", "content": severity_assessment_system_prompt},
        {"role": "user", "content": claim_info_json},
    ]

    response = get_completion(client, messages=messages)

    # Gate check: validate the severity assessment
    try:
        validated_severity = gate2_cost_range_ok(response)
        return validated_severity
    except ValueError as e:
        print(f"Gate 2 failed: {e}. Response: {response}")
        return None


# ------------------------------------------------------------------------------
class ClaimRouting(BaseModel):
    claim_id: str
    queue: Literal["glass", "fast_track", "material_damage", "total_loss"]


# Define a gate check function and assess_severity function
def gate3_validate_routing(routing_json: str) -> ClaimRouting:
    """
    Gate 3: Validates that the claim is routed to a valid queue.
    Returns validated ClaimRouting object or raises validation error.
    """
    try:
        # Parse the JSON string
        routing_dict = json.loads(routing_json)
        # Validate with Pydantic model
        validated_routing = ClaimRouting(**routing_dict)
        return validated_routing
    except Exception as e:
        raise ValueError(f"Gate 3 validation failed: {str(e)}")


def route_claim(
    client, 
    queue_routing_system_prompt: str, 
    claim_info: ClaimInformation, 
    severity_assessment: Optional[SeverityAssessment],
) -> Optional[ClaimRouting]:
    """
    Stage 3: Route claim to appropriate queue
    """
    if severity_assessment is None:
        return None

    # Create input for the routing model
    routing_input = f"""

        Based on the following claim information and severity assessment, please route the claim.

        Claim Information: {claim_info.model_dump_json(indent=2)}

        Severity Assessment: {severity_assessment.model_dump_json(indent=2)}
    
    """  # <-- Create a dictionary with the necessary information

    messages = [
        {"role": "system", "content": queue_routing_system_prompt},
        {"role": "user", "content": json.dumps(routing_input)},
    ]

    response = get_completion(client, messages=messages)

    # Gate check: validate the routing decision
    try:
        validated_routing = gate3_validate_routing(response)
        return validated_routing
    except ValueError as e:
        print(f"Gate 3 failed: {e}. Response: {response}")
        return None
