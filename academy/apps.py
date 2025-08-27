from django.apps import AppConfig


class AcademyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'academy'
    def ready(self):
        import logging
        logger = logging.getLogger(__name__)

        # Import extensions - this is crucial and must happen in ready()
        try:
            from academy.extensions import PartnerExtension  # This will register and apply extensions
            logger.info("Extensions imported successfully")
        except ImportError as e:
            logger.error(f"Failed to import extensions: {e}")
            return
        
        # Final check for any pending extensions
        try:
            from modules.base.model_inheritance import setup_model_extensions
            setup_model_extensions()
        except Exception as e:
            logger.error(f"Failed to setup extensions: {e}")
            import traceback
            traceback.print_exc()
