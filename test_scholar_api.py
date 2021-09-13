from scholarly import scholarly

query = scholarly.search_pubs(" Denoising Diffusion Probabilistic Models  ")
pub = next(query)
print(scholarly.bibtex(pub))