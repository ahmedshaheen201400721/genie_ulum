from django.apps import AppConfig


class AcademyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academy'
    # def ready(self):
    #     import logging
    #     logger = logging.getLogger(__name__)

    #     try:
    #         # from academy.extensions.teacher import TeacherExtension
    #         # from academy.extensions.lead import LeadExtension 
    #         # logger.info("Extensions imported successfully")
    #     except ImportError as e:
    #         logger.error(f"Failed to import extensions: {e}")
    #         return
        
    #     try:
    #         from modules.base.model_inheritance import setup_model_extensions
    #         setup_model_extensions()
    #     except Exception as e:
    #         logger.error(f"Failed to setup extensions: {e}")
    #         import traceback
    #         traceback.print_exc()
