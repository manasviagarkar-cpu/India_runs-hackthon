import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_candidates(job_description, candidates):
    """Ranks candidates based on TF-IDF cosine similarity to the job description."""
    
    # Combine job description text
    jd_text = f"{job_description['title']} {job_description['description']} {' '.join(job_description['requirements'])}"
    
    # Combine candidate texts
    candidate_texts = []
    for candidate in candidates:
        candidate_text = f"{candidate['resume_text']} {' '.join(candidate['skills'])}"
        candidate_texts.append(candidate_text)
    
    # All texts for vectorization
    all_texts = [jd_text] + candidate_texts
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Calculate cosine similarity between JD and all candidates
    jd_vector = tfidf_matrix[0:1]
    candidate_vectors = tfidf_matrix[1:]
    
    similarities = cosine_similarity(jd_vector, candidate_vectors).flatten()
    
    ranked_candidates = []
    for i, candidate in enumerate(candidates):
        similarity_score = similarities[i]
        
        # Additional scoring factors (e.g., experience match)
        experience_score = min(candidate['experience_years'] / 5.0, 1.0) * 0.2
        
        final_score = (similarity_score * 0.8) + experience_score
        
        ranked_candidates.append({
            "candidate_id": candidate['candidate_id'],
            "name": candidate['name'],
            "ranking_score": float(final_score)
        })
    
    # Sort candidates by final score in descending order
    ranked_candidates.sort(key=lambda x: x['ranking_score'], reverse=True)
    
    # Assign ranks
    for i, candidate in enumerate(ranked_candidates):
        candidate['rank'] = i + 1
        
    return ranked_candidates

def main():
    # Load sample data
    with open('sample_data.json', 'r') as f:
        data = json.load(f)
    
    job_description = data['job_description']
    candidates = data['candidates']
    
    # Rank candidates
    ranked_results = rank_candidates(job_description, candidates)
    
    # Output results
    print(json.dumps(ranked_results, indent=2))
    
    # Save results to CSV
    import csv
    with open('ranked_candidates.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["candidate_id", "name", "ranking_score", "rank"])
        writer.writeheader()
        writer.writerows(ranked_results)
    
    print("\nRanked candidates saved to ranked_candidates.csv")

if __name__ == "__main__":
    main()
