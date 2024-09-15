export type SelectorInputProps = {
    label_name: string;
    options: object;
    input_name: string;
    defaultValue: any;
    setValue: (input) => void;
}

export default function SelectorInput ({label_name, options, input_name, defaultValue, setValue}: SelectorInputProps) {
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
                    <select id={input_name} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" onChange={(e) => setValue(e.target.value)}>
                       {Object.entries(options).map(entry => {
                        
                        return <option value={entry[0]} selected={defaultValue == entry[0]}>{entry[1]}</option>})} 
                    </select>
                </div>
            </div>
        </div>
    )
}