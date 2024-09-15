'use client';

import FormInput from './FormInput';
import { FormInputType } from './types/FormInputType';
import { isValidRadius } from './form_validators/isValidRadius';
import { FormInputValues } from './types/FormInputValues';
import { SetStateAction, useState } from 'react';
import FormError from './FormError';
import { isValidNumberOfGores } from './form_validators/isValidNumberOfGores';
import SliderInput from './SliderInput';
import SelectorInput from './SelectorInput';
import { Units } from './types/Units';
import ComponentWrapper from './ComponentWrapper';
import { exec } from 'child_process';
import { cm_to_inches, mm_to_inches } from './convert_to_inches';

export default function Form() {
    const [radius, setRadius] = useState<number>();
    const [numGores, setNumGores] = useState<number>();
    const [precision, setPrecision] = useState<number>(50);
    const [unit, setUnit] = useState<Units>(Units.CM);
    const [radiusInputError, setRadiusInputError] = useState<boolean>(false);
    const [numGoresInputError, setNumGoresInputError] =
        useState<boolean>(false);
    const [previsionInputError, setPrecisionInputError] =
        useState<boolean>(false);
    const [otherFormError, setOtherFormError] = useState<boolean>(false);

    const validateFormInput = (event) => {
        event.preventDefault();
        const allInputsProvided = radius && numGores && precision;

        if (!allInputsProvided) {
            setOtherFormError(true);
            return;
        } else {
            setOtherFormError(false);
        }

        if (!isValidRadius(radius)) {
            setRadiusInputError(true);
        } else {
            setRadiusInputError(false);
        }

        if (!isValidNumberOfGores(numGores)) {
            setNumGoresInputError(true);
        } else {
            setNumGoresInputError(false);
        }

        if (isValidRadius(radius) && isValidNumberOfGores(numGores)) {
            let radius_input;
            switch(unit) {
                case (Units.CM) :
                    radius_input = cm_to_inches(radius)
                    break;
                case (Units.MM):
                    radius_input = mm_to_inches(radius)
                    break;
                case (Units.INCHES):
                    radius_input = radius;
            }
            
        }
    };

    return (
        <ComponentWrapper>
            <form
                onSubmit={validateFormInput}
                noValidate
            >
                <div className="space-y-12">
                    <div className="border-b border-gray-900/10 pb-12">
                        <p className="mt-1 text-sm leading-6 text-gray-600">
                            Enter the information of the desired hemisphere.
                        </p>

                        <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                            <SelectorInput
                                label_name={'Unit'}
                                options={Units}
                                input_name={'unit'}
                                defaultValue={unit}
                                setValue={setUnit}
                            />
                            <FormInput
                                input_name="radius"
                                setValue={setRadius}
                                errorMessage="Please input a valid radius. The radius needs to be a positive rational number."
                                step="any"
                                isError={radiusInputError}
                            />
                            <FormInput
                                input_name="number of gores"
                                setValue={setNumGores}
                                errorMessage="Please input a valid number of gores. The number of gores needs to be a natural number (1, 2, 3, ...)"
                                isError={numGoresInputError}
                            />
                            <SliderInput
                                input_name="precision"
                                input_type={FormInputType.RANGE}
                                min={0}
                                max={100}
                                setValue={setPrecision}
                                errorMessage="I do not know how you managed to break this"
                                isError={previsionInputError}
                            />
                        </div>
                        <div className="mt-5 text-sm leading-6 text-gray-600">
                            {otherFormError && (
                                <FormError errorMessage="All values must be provided." />
                            )}
                        </div>
                    </div>

                    <div className="mt-6 flex items-center justify-end gap-x-6">
                        <button
                            type="button"
                            className="text-sm font-semibold leading-6 text-gray-900"
                        >
                            Cancel
                        </button>
                        <button
                            type="submit"
                            className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 group-invalid:pointer-events-none group-invalid:opacity-30"
                        >
                            Generate
                        </button>
                    </div>
                </div>
            </form>
        </ComponentWrapper>
    );
}
