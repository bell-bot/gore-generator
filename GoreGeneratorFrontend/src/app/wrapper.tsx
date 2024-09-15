'use client'

import { StaticImageData } from 'next/image';
import Form from './form'
import OutputWrapper from './GeneratorOutput'
import { useState } from 'react';

export default function Wrapper() {

    const [generatorOutput, setGeneratorOutput] = useState<StaticImageData>();

    return (
        <>
            <div className="min-h-full">
                <header className="bg-gray-700 shadow">
                    <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                        <h1 className="text-4xl font-bold tracking-tight text-indigo-50 text-center">
                            Gore Generator
                        </h1>
                    </div>
                </header>
                <main>
                    <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                        <div className="flex flex-row gap-5">
                            <Form />
                            <OutputWrapper />
                        </div>
                    </div>
                </main>
            </div>
        </>
    )
}
