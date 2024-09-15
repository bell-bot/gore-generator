import { isPositiveNumber } from './isPositiveNumber'

export function isValidNumberOfGores(n: number) {
    return Number.isInteger(Number(n)) && isPositiveNumber(n)
}
