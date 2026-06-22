# The Data & AI Challenge: Intelligent Candidate Ranking System
 
## Overview

This repository contains the solution for "The Data & AI Challenge" in the India Runs hackathon. The goal of this project is to build an AI-powered candidate ranking system that moves beyond traditional keyword matching to semantically understand job descriptions and candidate profiles. The system aims to deliver a ranked shortlist of candidates that a recruiter can trust, by holistically evaluating career history, skills, behavioral signals, and platform activity.

## Challenge Requirements Addressed

*   **Semantic Job Description Understanding:** The system interprets job descriptions to grasp underlying requirements and nuances, not just keywords.
*   **Holistic Candidate Evaluation:** Candidate profiles are analyzed comprehensively, considering various data points to assess genuine fit.
*   **Trustworthy Shortlist Generation:** A ranked list of candidates is produced, providing recruiters with an actionable and reliable tool.
*   **Flexible AI Architecture:** The solution demonstrates a hybrid approach combining TF-IDF for semantic similarity and custom feature engineering for experience-based scoring.

## System Architecture

The AI pipeline consists of the following modules:

1.  **Data Ingestion:** Loads job descriptions and candidate profiles.
2.  **Text Preprocessing:** Cleans and normalizes textual data.
3.  **TF-IDF Vectorization:** Converts text into numerical representations capturing semantic importance.
4.  **Feature Engineering:** Extracts structured features like years of experience.
5.  **Hybrid Ranking Model:** Combines semantic similarity (TF-IDF cosine similarity) with engineered features to generate a final ranking score.
6.  **Output Generation:** Produces a ranked CSV file of candidates.


1.  **View results:**
    The script will print the ranked candidates to the console and save them to a CSV file named `ranked_candidates.csv` in the following format:

    | Field Name       | Data Type | Description                                          |
    | :--------------- | :-------- | :--------------------------------------------------- |
    | `candidate_id`   | String    | Unique identifier for the candidate                  |
    | `ranking_score`  | Float     | A numerical score indicating the candidate's fit (higher is better) |
    | `rank`           | Integer   | The final rank of the candidate (1st, 2nd, 3rd, etc.) |

