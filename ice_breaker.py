from typing import Tuple

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linedin_profile
from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel

def ice_break(name: str) -> Tuple[PersonIntel, str, str]:

  print("Entered ice breaker method")
  linkedin_profile_url = linkedin_lookup_agent(name=name)

  summary_template ="""
       given the Linkedin information {information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
         {format_instructions}
  """
  # reservation_template = '''
  #   Book us a nice table for two this Friday at 6:00 PM. 
  #   Choose any cuisine, it doesn't matter. Send the confirmation by email.

  #   Our location is: {query}

  #   Format instructions:
  #   {format_instructions}
  # '''

  print(person_intel_parser.get_format_instructions())
  summary_prompt_template = PromptTemplate(
                              input_variables=["information"], 
                              template=summary_template,
                              partial_variables={
                                "format_instructions": person_intel_parser.get_format_instructions()
                              }
                            )

  print(summary_prompt_template)
  llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

  chain = LLMChain(llm=llm, prompt=summary_prompt_template)

  linkedin_data = scrape_linedin_profile(linkedin_profile_url=linkedin_profile_url)

  result = chain.run(information=linkedin_data)

  print("+++++++++")
  print(result)
  print(person_intel_parser.parse(result))
  # return result
  return person_intel_parser.parse(result), linkedin_data.get("profile_pic_url"), linkedin_profile_url

# if __name__ == '__main__':
#   print("Hello LangChain")
#   result = ice_break("Kalvakuntla Taraka Rama Rao")
#   #print(result)
#   #print(scrape_user_tweets(username="naveenkarumuru"))


