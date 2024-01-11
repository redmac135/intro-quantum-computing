from dimod import BinaryQuadraticModel

bqm = BinaryQuadraticModel(
    {"t": 1, "v": 1, "l": -1}, {"tv": -2, "tl": 1, "tp": -1}, 1, "BINARY"
)
from dwave.system import DWaveSampler, EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=5000, label="Example - Workshop")
print(sampleset.lowest(atol=0.5))
