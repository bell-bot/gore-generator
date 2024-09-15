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
    isError: boolean
};

export default function FormInput({
    input_name,
    input_type,
    min,
    max,
    default_value,
    setValue,
    errorMessage,
    step,
    isError
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
                <div className="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                    <span className="flex select-none items-center pl-6 text-gray-500 sm:text-sm"></span>
                    <input
                        id={input_name}
                        name={input_name}
                        type={input_type ?? 'number'}
                        className="block flex-1 border-0 bg-transparent py-1.5 pl-2 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                        onChange={(e) => setValue(e.target.value)}
                        value={default_value}
                        min={min}
                        max={max}
                        required
                        step={step}
                    />
                </div>
                {isError && <FormError errorMessage={errorMessage}/>}
            </div>
        </div>
    );
}
