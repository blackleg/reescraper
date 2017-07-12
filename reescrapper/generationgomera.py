from .core import GenerationScrapper


class GenerationGomera(GenerationScrapper):

    def __init__(self):
        super().__init__()
        self.url = "https://demanda.ree.es/movil/canarias/la_gomera/tablas/2"

    def get(self):
        return self._get(self.url)
