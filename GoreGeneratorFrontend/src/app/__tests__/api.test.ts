import { RequestParameters } from '../types/RequestParameters';
import { parseQueryParameters } from '../api';
import '@testing-library/jest-dom';

describe('parseQueryParameters', () => {
    it('returns formatted query string', () => {
        const queryParameters: RequestParameters = {
            radius: 10.9,
            n_gores: 6,
            precision: 56,
        };

        const expected = 'radius=10.9&n_gores=6&precision=56';
        const actual = parseQueryParameters(queryParameters);

        expect(expected).toEqual(actual);
    });
});
