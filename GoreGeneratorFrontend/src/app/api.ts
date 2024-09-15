import { RequestParameters } from './types/RequestParameters';

export function parseQueryParameters(parameters: RequestParameters): string {
    return Object.entries(parameters).join('&');
}

export function submit(formData: RequestParameters) {}
