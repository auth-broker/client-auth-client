from typing import Annotated, Union
from pydantic import Field

from .OAuth2AuthorizeResponse import OAuth2AuthorizeResponse
from .PKCEAuthorizeResponse import PKCEAuthorizeResponse

AuthorizeResponse = Annotated[Union[OAuth2AuthorizeResponse, PKCEAuthorizeResponse], Field(discriminator="type")]
