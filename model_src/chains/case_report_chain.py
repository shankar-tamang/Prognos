from langchain_core.output_parsers import StrOutputParser
from llm_provider import get_gemini_llm
from chains.prompts.report_prompt_template import REPORT_PROMPT_TEMPLATE
from langchain_core.prompts import PromptTemplate
from utils.logging_utils import logger

def create_case_report_chain(model_name="gemini-2.0-flash", temperature=0):
    try:
        llm = get_gemini_llm(model_name=model_name, temperature=temperature)
        prompt = PromptTemplate.from_template(REPORT_PROMPT_TEMPLATE)
        chain = prompt | llm | StrOutputParser()
        return chain
    except Exception as e:
        logger.error(f"Error creating case report chain: {e}")
        raise
