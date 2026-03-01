from __future__ import annotations

import json
from collections.abc import AsyncGenerator
from typing import Any, Dict, Optional, Union

import httpx
from pydantic import BaseModel, TypeAdapter

from ..exceptions import HTTPException
from ..models import *


class AsyncClient(BaseModel):
    model_config = {"validate_assignment": True}

    base_url: str = "/"
    verify: Union[bool, str] = True
    access_token: Optional[str] = None

    async def get_access_token(self) -> Optional[str]:
        return self.access_token

    async def set_access_token(self, value: str) -> None:
        self.access_token = value

    async def get_login_url_login_post(
        self,
        data: LoginRequest,
    ) -> AuthorizeResponse:
        base_url = self.base_url
        path = f"/login"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        _token = await self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {}
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        async with httpx.AsyncClient(base_url=base_url, verify=self.verify) as client:
            response = await client.request(
                "post",
                httpx.URL(path),
                headers=headers,
                params=query_params,
                json=data.model_dump(by_alias=True, exclude_none=True),
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"get_login_url_login_post failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(AuthorizeResponse).validate_python(body)

    async def callback_callback_get(
        self,
        redirect_url: Optional[Union[str, None]] = None,
    ) -> OAuth2TokenExposed:
        base_url = self.base_url
        path = f"/callback"

        headers = {
            "Accept": "application/json",
        }

        _token = await self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {
            "redirect_url": redirect_url,
        }
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        async with httpx.AsyncClient(base_url=base_url, verify=self.verify) as client:
            response = await client.request(
                "get",
                httpx.URL(path),
                headers=headers,
                params=query_params,
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"callback_callback_get failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(OAuth2TokenExposed).validate_python(body)

    async def refresh_token_refresh_post(
        self,
        data: RefreshTokenRequest,
    ) -> OAuth2TokenExposed:
        base_url = self.base_url
        path = f"/refresh"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        _token = await self.get_access_token()
        if _token:
            headers["Authorization"] = f"Bearer {_token}"

        query_params: Dict[str, Any] = {}
        query_params = {k: v for (k, v) in query_params.items() if v is not None}

        async with httpx.AsyncClient(base_url=base_url, verify=self.verify) as client:
            response = await client.request(
                "post",
                httpx.URL(path),
                headers=headers,
                params=query_params,
                json=data.model_dump(by_alias=True, exclude_none=True),
            )

        if response.status_code != 200:
            raise HTTPException(
                response.status_code,
                f"refresh_token_refresh_post failed with status code: {response.status_code}",
            )

        body = None if 200 == 204 else response.json()

        return TypeAdapter(OAuth2TokenExposed).validate_python(body)
