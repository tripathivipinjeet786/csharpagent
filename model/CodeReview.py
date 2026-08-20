from pydantic import BaseModel, Field
from typing import Literal

class CodeIssue(BaseModel):
    severity: Literal["critical", "high", "medium", "low", "info"]
    category: Literal[
        "bug",
        "security",
        "performance",
        "maintainability",
        "design",
        "style",
        "testing",
        "other",
    ]
    title: str
    explanation: str
    suggestion: str
    line_number: int | None = None


class CodeReviewResult(BaseModel):
    status: Literal["PASS", "FAIL"]
    summary: str
    issues: list[CodeIssue] = Field(default_factory=list)
    fixed_code_required: bool