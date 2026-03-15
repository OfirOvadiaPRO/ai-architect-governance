from typing import List, Set

class RAGMetrics:
    """
    Enterprise-grade evaluation metrics for Retrieval-Augmented Generation.
    """
    @staticmethod
    def compute_hit_rate(retrieved_ids: List[str], ground_truth_ids: Set[str]) -> float:
        """
        Calculates if the correct document was in the top-k results.
        """
        if not ground_truth_ids:
            return 0.0
        hits = any(rid in ground_truth_ids for rid in retrieved_ids)
        return 1.0 if hits else 0.0

    @staticmethod
    def compute_mrr(retrieved_ids: List[str], ground_truth_ids: Set[str]) -> float:
        """
        Calculates Mean Reciprocal Rank for the retrieval set.
        """
        for i, rid in enumerate(retrieved_ids):
            if rid in ground_truth_ids:
                return 1.0 / (i + 1)
        return 0.0
