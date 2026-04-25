import json
import asyncio
import os
import getpass

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

load_dotenv()

# Check for OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY environment variable not set.")
    print("Running in mock mode for demonstration purposes.")
    print("To use actual AI capabilities, set your OpenAI API key.")

class paper(BaseModel):
    title: str
    
    authors: list[str]
    year: int
    venue: str | None= None
    url: str | None = None
    relevance: str = Field(description='whyy its relevant')



class Formula(BaseModel):
    name : str
    latex : str = Field(description='the latex code for the formula')
    description : str
    reference : str | None = Field(default=None, description='a reference to the paper or source where this formula is used')    
  



class trend(BaseModel):
    title: str
    
    description : str

    references: list[str] = Field(default_factory=list, description="urls backing this trend")

class Report(BaseModel):
    topics: str
    research_questions: list[str]
    time_frame: str | None = None
    papers: list[paper] = Field(description="6 to 9 most relvant papers")
    formulas:list[Formula]
    trends: list[trend]




async def main():
    topic = input("Enter the research topic: ").strip()
    questions = input("key research questions ").strip()
    time_frame = input("WHAT TIME froma should the papers be from ").strip()


    task = f"""topic: {topic}
Research questions: {questions}
time frame: {time_frame or 'no specific focus'}


Gather 6- 9 highly relevant papers
then identify most mathmatical formulas fort his subjesct and recent trends.StopAsyncIteration
populate the report schema fully."""


    # Initialize model
    if not os.getenv("OPENAI_API_KEY"):
        # Create a mock model that returns sample data
        from langchain_core.messages import AIMessage
        
        class MockChatModel:
            def __init__(self):
                pass
            
            def with_structured_output(self, output_schema, method="function_calling"):
                return self
            
            async def ainvoke(self, messages):
                # Return a mock response that matches the Report schema
                from datetime import datetime
                current_year = datetime.now().year
                
                # Create mock data
                mock_papers = [
                    {
                        "title": "Menstrual Cycle Effects on Mood and Emotional Regulation",
                        "authors": ["Smith, J.A.", "Johnson, L.M.", "Williams, K.R."],
                        "year": 2025,
                        "venue": "Journal of Women's Health",
                        "url": "https://doi.org/10.1093/jwh/whab123",
                        "relevance": "Directly examines hormonal fluctuations during menstrual cycle and their impact on mood disorders"
                    },
                    {
                        "title": "Estrogen and Serotonin Interactions in Premenstrual Dysphoric Disorder",
                        "authors": ["Garcia, M.R.", "Chen, Y.L.", "Rodriguez, A.B."],
                        "year": 2024,
                        "venue": "Molecular Psychiatry",
                        "url": "https://doi.org/10.1038/s41380-024-01456-7",
                        "relevance": "Explains neurochemical mechanisms linking ovarian hormones to mood symptoms"
                    },
                    {
                        "title": "Longitudinal Study of Mood Variability Across the Menstrual Cycle",
                        "authors": ["Thompson, R.K.", "Davis, S.P.", "Miller, J.H."],
                        "year": 2025,
                        "venue": "Psychoneuroendocrinology",
                        "url": "https://doi.org/10.1016/j.psyneuen.2025.105678",
                        "relevance": "Provides empirical data on mood changes throughout different menstrual phases"
                    }
                ]
                
                mock_formulas = [
                    {
                        "name": "Free Androgen Index",
                        "latex": "FAI = \\frac{\\text{Total Testosterone (nmol/L)}}{\\text{SHBG (nmol/L)}} \\times 100",
                        "description": "Calculates bioavailability of testosterone by accounting for sex hormone-binding globulin levels",
                        "reference": "Smith et al. (2025)"
                    },
                    {
                        "name": "Luteinizing Hormone to Follicle Stimulating Hormone Ratio",
                        "latex": "LH/FSH Ratio",
                        "description": "Used to assess ovarian function and predict ovulation timing",
                        "reference": "Garcia et al. (2024)"
                    }
                ]
                
                mock_trends = [
                    {
                        "title": "Digital Tracking of Menstrual Symptoms",
                        "description": "Increasing use of mobile apps for real-time mood and symptom tracking throughout menstrual cycle",
                        "references": [
                            "https://www.nature.com/articles/s41598-024-56789-0",
                            "https://doi.org/10.1002/ab.21987"
                        ]
                    },
                    {
                        "title": "Personalized Medicine Approaches to PMDD",
                        "description": "Tailoring treatment based on individual hormonal profiles and genetic markers",
                        "references": [
                            "https://doi.org/10.1016/j.ygyno.2024.01.005",
                            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7890123/"
                        ]
                    }
                ]
                
                # Create and return mock result
                mock_result = {
                    "topics": topic,
                    "research_questions": questions.split(", ") if ", " in questions else [questions],
                    "time_frame": time_frame,
                    "papers": mock_papers,
                    "formulas": mock_formulas,
                    "trends": mock_trends
                }
                
                # Convert to proper format
                from pydantic import BaseModel
                class MockReport(BaseModel):
                    topics: str
                    research_questions: list[str]
                    time_frame: str | None = None
                    papers: list = []
                    formulas: list = []
                    trends: list = []
                
                report_obj = MockReport(**mock_result)
                return AIMessage(content=report_obj.model_dump_json())
        
        model = MockChatModel()
    else:
        model = init_chat_model("gpt-4-0613", model_provider="openai").with_structured_output(Report, method="function_calling")

    result = await model.ainvoke([
        {'role': 'system', 'content':  'you are a pro research assistant in writing academic papers and thesis'},
        {'role': 'user', 'content': task}
    ])
    print(json.dumps(result.model_dump(), indent=2))



asyncio.run(main())