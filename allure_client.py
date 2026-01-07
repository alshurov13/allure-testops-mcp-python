"""
Allure TestOps REST API Client
Provides HTTP methods for interacting with Allure TestOps API
"""

import json
from typing import Any
from urllib.parse import urljoin
import httpx


class AllureClient:
    """HTTP client for Allure TestOps API"""
    
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.token = token
    
    def _get_headers(self) -> dict[str, str]:
        """Get HTTP headers for API requests"""
        return {
            'Authorization': f'Api-Token {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
    
    def _build_url(self, path: str, params: dict[str, Any] | None = None) -> str:
        """Build full URL with query parameters"""
        url = urljoin(self.base_url, path)
        if params:
            # Filter out None values and handle arrays
            filtered_params = {}
            for key, value in params.items():
                if value is not None:
                    if isinstance(value, list):
                        # For arrays, we need to append each value
                        filtered_params[key] = value
                    else:
                        filtered_params[key] = value
            
            # Build query string manually to handle arrays
            query_parts = []
            for key, value in filtered_params.items():
                if isinstance(value, list):
                    for item in value:
                        query_parts.append(f"{key}={item}")
                else:
                    query_parts.append(f"{key}={value}")
            
            if query_parts:
                url += '?' + '&'.join(query_parts)
        
        return url
    
    async def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        """Perform GET request"""
        url = self._build_url(path, params)
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
    
    async def post(self, path: str, body: Any | None = None, params: dict[str, Any] | None = None) -> Any:
        """Perform POST request"""
        url = self._build_url(path, params)
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                headers=self._get_headers(),
                json=body if body else None
            )
            response.raise_for_status()
            return response.json()
    
    async def patch(self, path: str, body: Any, params: dict[str, Any] | None = None) -> Any:
        """Perform PATCH request"""
        url = self._build_url(path, params)
        async with httpx.AsyncClient() as client:
            response = await client.patch(
                url,
                headers=self._get_headers(),
                json=body
            )
            response.raise_for_status()
            return response.json()
    
    async def put(self, path: str, body: Any, params: dict[str, Any] | None = None) -> Any:
        """Perform PUT request"""
        url = self._build_url(path, params)
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url,
                headers=self._get_headers(),
                json=body
            )
            response.raise_for_status()
            return response.json()
    
    async def delete(self, path: str, params: dict[str, Any] | None = None) -> None:
        """Perform DELETE request"""
        url = self._build_url(path, params)
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=self._get_headers())
            response.raise_for_status()
    
    # Test Case CRUD
    async def get_test_cases(self, project_id: str, params: dict[str, Any] | None = None) -> Any:
        """Get all test cases for a project"""
        query_params = {"projectId": project_id}
        if params:
            query_params.update(params)
        return await self.get("/api/rs/testcase", query_params)
    
    async def get_test_case(self, test_case_id: int) -> Any:
        """Get a specific test case by ID"""
        return await self.get(f"/api/rs/testcase/{test_case_id}")
    
    async def create_test_case(self, project_id: str, test_case: dict[str, Any]) -> Any:
        """Create a new test case"""
        body = {**test_case, "projectId": int(project_id)}
        return await self.post("/api/rs/testcase", body)
    
    async def update_test_case(self, test_case_id: int, test_case: dict[str, Any]) -> Any:
        """Update an existing test case"""
        return await self.patch(f"/api/rs/testcase/{test_case_id}", test_case)
    
    async def delete_test_case(self, test_case_id: int) -> None:
        """Delete a test case"""
        await self.delete(f"/api/rs/testcase/{test_case_id}")
    
    async def bulk_create_test_cases(self, project_id: str, test_cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Bulk create test cases"""
        results = []
        for test_case in test_cases:
            try:
                result = await self.create_test_case(project_id, test_case)
                results.append({"success": True, "data": result})
            except Exception as e:
                results.append({"success": False, "error": str(e), "testCase": test_case})
        return results
    
    # Launch CRUD
    async def get_launches(self, project_id: str, params: dict[str, Any] | None = None) -> Any:
        """Get all launches for a project"""
        query_params = {"projectId": project_id}
        if params:
            query_params.update(params)
        return await self.get("/api/rs/launch", query_params)
    
    async def get_launch(self, launch_id: int) -> Any:
        """Get a specific launch by ID"""
        return await self.get(f"/api/rs/launch/{launch_id}")
    
    async def create_launch(self, project_id: str, launch: dict[str, Any]) -> Any:
        """Create a new launch"""
        body = {**launch, "projectId": int(project_id)}
        return await self.post("/api/rs/launch", body)
    
    async def update_launch(self, launch_id: int, launch: dict[str, Any]) -> Any:
        """Update an existing launch"""
        return await self.patch(f"/api/rs/launch/{launch_id}", launch)
    
    async def delete_launch(self, launch_id: int) -> None:
        """Delete a launch"""
        await self.delete(f"/api/rs/launch/{launch_id}")
    
    async def close_launch(self, launch_id: int) -> Any:
        """Close a launch"""
        return await self.post(f"/api/rs/launch/{launch_id}/close")
    
    # Test Plan CRUD
    async def get_test_plans(self, project_id: str, params: dict[str, Any] | None = None) -> Any:
        """Get all test plans for a project"""
        query_params = {"projectId": project_id}
        if params:
            query_params.update(params)
        return await self.get("/api/rs/testplan", query_params)
    
    async def get_test_plan(self, test_plan_id: int) -> Any:
        """Get a specific test plan by ID"""
        return await self.get(f"/api/rs/testplan/{test_plan_id}")
    
    async def create_test_plan(self, project_id: str, test_plan: dict[str, Any]) -> Any:
        """Create a new test plan"""
        body = {**test_plan, "projectId": int(project_id)}
        return await self.post("/api/rs/testplan", body)
    
    async def update_test_plan(self, test_plan_id: int, test_plan: dict[str, Any]) -> Any:
        """Update an existing test plan"""
        return await self.patch(f"/api/rs/testplan/{test_plan_id}", test_plan)
    
    async def delete_test_plan(self, test_plan_id: int) -> None:
        """Delete a test plan"""
        await self.delete(f"/api/rs/testplan/{test_plan_id}")


def create_allure_client(base_url: str, token: str) -> AllureClient:
    """Create and return AllureClient instance"""
    return AllureClient(base_url, token)

