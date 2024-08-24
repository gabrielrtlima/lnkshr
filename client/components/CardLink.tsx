import InputWithCopy from "./Input";
import { ModeToggle } from "./ModeToggle";

export default function CardLink() {
  return (
    <div className="flex flex-col bg-background bg-opacity-30 backdrop-blur-3xl rounded-lg shadow-lg w-5/12 h-1/4">
      <h1 className="text-6xl font-sans font-black text-center pt-4">lnkshr</h1>

      <ModeToggle />
      <div className="flex h-2/4 justify-center items-center">
        <InputWithCopy />
      </div>
    </div>
  )
}
