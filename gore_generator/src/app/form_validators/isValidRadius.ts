import { isPositiveNumber } from './isPositiveNumber'

export function isValidRadius(radius: number) {
    return isPositiveNumber(radius)
}
