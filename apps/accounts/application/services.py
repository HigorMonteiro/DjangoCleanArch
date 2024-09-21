from apps.accounts.infrastructure.linkedin_gateway import LinkedInGateway
from apps.accounts.infrastructure.openai_gateway import OpenAIGateway
from apps.accounts.infrastructure.repositories import UserRepository


class UserService:
    """
    This class provides methods for interacting with user data.

    Methods:
    - get_linkedin_info(linkedin_url): Fetches user information from LinkedIn.
    - generate_user_embeddings(linkedin_info): Generates embeddings for user summary.
    - save_user(user_data, linkedin_info, embeddings): Saves user data to the repository.
    """

    @staticmethod
    def get_linkedin_info(linkedin_url):
        return LinkedInGateway.fetch_user_info(linkedin_url)

    @staticmethod
    def generate_user_embeddings(linkedin_info):
        return OpenAIGateway.generate_embeddings(linkedin_info['summary'])

    @staticmethod
    def save_user(user_data, linkedin_info, embeddings):
        user = {
            "name": user_data['name'],
            "email": user_data['email'],
            "linkedin_id": linkedin_info['id'],
            "summary_embeddings": embeddings
        }
        return UserRepository.save(user)
