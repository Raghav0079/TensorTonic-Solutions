def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x1 = max(box_a[0] , box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])

    inner_width = max(0, x2-x1)
    inner_height = max(0,y2-y1)
    intersection_area = inner_width*inner_height

    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    union_area = area_a + area_b - intersection_area

    if union_area == 0: 
        return 0.0

    return intersection_area/union_area