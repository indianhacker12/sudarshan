#!/usr/bin/env python3
"""
API Security Testing Module for Sudarshan AI Security Scanner
Comprehensive REST/GraphQL/SOAP API vulnerability testing
"""

import asyncio
import aiohttp
import json
from typing import Dict, List, Any
from urllib.parse import urljoin

class APISecurityScanner:
    """Advanced API security testing"""
    
    def __init__(self, config, logger, ai_engine):
        self.config = config
        self.logger = logger
        self.ai_engine = ai_engine
        self.vulnerabilities = []
    
    async def scan_api_endpoints(self) -> List[Dict[str, Any]]:
        """Comprehensive API security testing"""
        
        # Discover API endpoints
        endpoints = await self.discover_api_endpoints()
        
        for endpoint in endpoints:
            # Test authentication bypass
            await self.test_auth_bypass(endpoint)
            
            # Test rate limiting
            await self.test_rate_limiting(endpoint)
            
            # Test input validation
            await self.test_input_validation(endpoint)
            
            # Test business logic flaws
            await self.test_business_logic(endpoint)
        
        return self.vulnerabilities
    
    async def discover_api_endpoints(self) -> List[str]:
        """AI-powered API endpoint discovery"""
        
        # Common API paths
        api_paths = [
            '/api/v1/', '/api/v2/', '/rest/', '/graphql',
            '/swagger/', '/openapi.json', '/api-docs'
        ]
        
        discovered = []
        for path in api_paths:
            try:
                url = urljoin(self.config.target_url, path)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            discovered.append(url)
            except:
                continue
        
        return discovered
    
    async def test_auth_bypass(self, endpoint: str):
        """Test for authentication bypass vulnerabilities"""
        
        bypass_techniques = [
            {'headers': {'X-Forwarded-For': '127.0.0.1'}},
            {'headers': {'X-Real-IP': '127.0.0.1'}},
            {'headers': {'X-Originating-IP': '127.0.0.1'}},
            {'headers': {'Authorization': 'Bearer null'}},
            {'headers': {'Authorization': 'Bearer admin'}},
        ]
        
        for technique in bypass_techniques:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(endpoint, **technique) as response:
                        if response.status == 200:
                            self.vulnerabilities.append({
                                'type': 'API Authentication Bypass',
                                'severity': 'High',
                                'endpoint': endpoint,
                                'technique': technique,
                                'description': 'API endpoint accessible without proper authentication'
                            })
            except:
                continue