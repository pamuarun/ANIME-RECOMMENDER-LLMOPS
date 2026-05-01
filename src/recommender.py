from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from src.prompt_template import get_anime_prompt


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):

        # 🔹 Main LLM (answer generator)
        self.llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=0.3
        )

        # 🔹 Query understanding LLM (lightweight reasoning)
        self.query_llm = ChatGroq(
            api_key=api_key,
            model=model_name,
            temperature=0.1
        )

        self.prompt = get_anime_prompt()

        # 🔹 Core RAG chain
        self.chain = (
            {
                "context": retriever | RunnableLambda(format_docs),
                "question": RunnablePassthrough(),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    # =========================
    # 🧠 QUERY ENRICHMENT
    # =========================
    def enrich_query(self, query: str) -> str:
        try:
            prompt = f"""
You are an anime recommendation query enhancer.

Convert the user query into a rich search query that captures:
- genre
- mood
- themes
- similar anime (if mentioned)
- emotional tone

User Query:
{query}

Enhanced Query:
"""
            result = self.query_llm.invoke(prompt).content.strip()

            return result if result else query

        except Exception:
            return query

    # =========================
    # 🎯 MAIN FUNCTION
    # =========================
    def get_recommendation(self, query: str):

        # Step 1: enrich query (VERY IMPORTANT)
        improved_query = self.enrich_query(query)

        # Step 2: run RAG chain
        return self.chain.invoke(improved_query)