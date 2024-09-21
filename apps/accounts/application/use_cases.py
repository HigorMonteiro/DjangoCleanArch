from .services import UserService

class RegisterUserUseCase:
    @staticmethod
    def execute(user_data):
        linkedin_info = UserService.get_linkedin_info(user_data['linkedin_url'])
        embeddings = UserService.generate_user_embeddings(linkedin_info)        
        user = UserService.save_user(user_data, linkedin_info, embeddings)
        
        return user
