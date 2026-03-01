from typing import *

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """
    LoginRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    scope: Optional[str] = Field(validation_alias="scope", default="openid email profile offline_access")

    response_type: Optional[str] = Field(validation_alias="response_type", default="code")

    identity_provider: Optional[Union[str, None]] = Field(validation_alias="identity_provider", default="Google")

    app_context: Optional[Dict[str, Any]] = Field(validation_alias="app_context", default=None)
