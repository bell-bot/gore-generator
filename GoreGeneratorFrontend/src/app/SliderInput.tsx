'use client';

import FormError from './FormError';
import { FormInputType } from './types/FormInputType';

type FormInputProps = {
    input_name: string;
    input_type?: FormInputType;
    min?: number;
    max?: number;
    default_value?: number;
    setValue: (input) => void;
    errorMessage: string;
    step?: string;
    isError: boolean;
};

export default function SliderInput({
    input_name,
    input_type,
    min,
    max,
    default_value,
    setValue,
    errorMessage,
    step,
    isError,
}: FormInputProps) {
    const label_name = input_name.charAt(0).toUpperCase() + input_name.slice(1);

    return (
        <div className="sm:col-span-4">
            <label
                htmlFor={input_name}
                className="block text-sm font-medium leading-6 text-gray-900"
            >
                {label_name}
            </label>
            <div className="mt-2">
                <div className="relative mb-6">
                    <input
                        id={input_name}
                        name={input_name}
                        type="range"
                        className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
                        onChange={(e) => setValue(e.target.value)}
                        value={default_value}
                        min={min}
                        max={max}
                        required
                        step={step}
                    />
                    <span className="text-sm text-gray-500 dark:text-gray-400 absolute start-0 -bottom-6">
                        low
                    </span>
                    <span className="text-sm text-gray-500 dark:text-gray-400 absolute end-0 -bottom-6">
                        high
                    </span>
                </div>
                {isError && <FormError errorMessage={errorMessage} />}
            </div>
        </div>
    );
}
