from event_manager import EventManager
from cert_generator import CertGenerator
from trainer_manager import TrainerManager

# event_manager = EventManager()
# print(event_manager.get_org_events())

# cert_generator = CertGenerator()
# cert_generator.generate_certs()

trainer_manager = TrainerManager()
print(trainer_manager.get_trainers())
