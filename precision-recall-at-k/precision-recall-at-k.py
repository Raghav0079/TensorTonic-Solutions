def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    if k <= 0 or not relevant:
        return [0.0, 0.0]
    
    # Take top k recommendations
    rec_k = recommended[:k]
    
    if not rec_k:
        return [0.0, 0.0]
    
    relevant_set = set(relevant)
    
    # Count unique relevant items in top k
    hits = len(set(rec_k) & relevant_set)
    
    precision = hits / k
    recall = hits / len(relevant_set)
    
    return [float(precision), float(recall)]