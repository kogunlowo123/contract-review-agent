"""Contract Review Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_contract():
    """Test Analyze a contract for key terms, obligations, and risks."""
    tools = AgentTools()
    result = await tools.analyze_contract(document="test", contract_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_risks():
    """Test Identify risky or unusual clauses in a contract."""
    tools = AgentTools()
    result = await tools.identify_risks(contract_id="test", risk_categories="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_compare_to_playbook():
    """Test Compare contract terms against company standard playbook."""
    tools = AgentTools()
    result = await tools.compare_to_playbook(contract_id="test", playbook="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_redlines():
    """Test Generate redline suggestions for non-standard terms."""
    tools = AgentTools()
    result = await tools.generate_redlines(contract_id="test", deviation_threshold="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.contract_review_agent_agent import ContractReviewAgentAgent
    agent = ContractReviewAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
