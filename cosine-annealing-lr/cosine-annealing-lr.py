import math

def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    # Ensure current_step doesn't exceed total_steps for safe bound calculation
    current_step = min(current_step, total_steps)
    
    if total_steps == 0:
        return float(base_lr)
        
    # Standard Cosine Annealing equation:
    # lr = min_lr + 0.5 * (base_lr - min_lr) * (1 + cos(pi * current_step / total_steps))
    cos_inner = math.pi * (current_step / total_steps)
    lr = min_lr + 0.5 * (base_lr - min_lr) * (1.0 + math.cos(cos_inner))
    
    return float(lr)