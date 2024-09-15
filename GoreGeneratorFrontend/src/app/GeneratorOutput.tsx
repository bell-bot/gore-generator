import { StaticImageData } from "next/image";
import ComponentWrapper from "./ComponentWrapper";
import OutputPlaceholder from "./OutputPlaceholder";

export type GeneratorOutputProps = {
    generatorOutput?: StaticImageData
}

export default function GeneratorOutput({generatorOutput}: GeneratorOutputProps) {
    return (
        <ComponentWrapper className="flex-grow">
            { generatorOutput ? <div></div> : <OutputPlaceholder/>}
            
        </ComponentWrapper>
    )
}