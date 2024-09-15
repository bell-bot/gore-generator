const CM_CONSTANT: number = 2.54;

export function cm_to_inches(cm_value: number): number {
    return cm_value / CM_CONSTANT;
}

export function mm_to_inches(mm_value: number): number {
    return mm_value / (CM_CONSTANT * 10);
}
