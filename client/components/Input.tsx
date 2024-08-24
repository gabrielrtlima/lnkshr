"use client"
import React, { useState } from 'react';
import { Copy, Check, ArrowBigRightDash } from "lucide-react";

export default function InputWithCopy() {
  const [inputValue, setInputValue] = useState('');
  const [generatedLink, setGeneratedLink] = useState('');
  const [isCopied, setIsCopied] = useState(false);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const generateLink = () => {
    // Simula a geração de um link encurtado
    const shortLink = `https://lnkshr.com/${Math.random().toString(36).substr(2, 6)}`;
    setGeneratedLink(shortLink);
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(generatedLink).then(() => {
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000);
    });
  };

  return (
    <div className="w-5/6 flex flex-col items-center space-y-4">
      <input
        type="text"
        value={generatedLink || inputValue}
        onChange={handleInputChange}
        placeholder="Enter your link"
        readOnly={!!generatedLink}
        className={`w-full py-2 px-4 bg-secondary text-muted-foreground font-sans bg-opacity-20 backdrop-blur-lg rounded-lg focus:outline-none focus:ring-2 focus:ring-muted-foreground transition duration-300 ease-in-out`}
      />
      {!generatedLink ? (
        <button
          onClick={generateLink}
          className="px-4 py-2 bg-transparent text-primary rounded-lg hover:bg-primary/10 transition duration-300 ease-in-out"
        >
          <ArrowBigRightDash size={20} />
        </button>
      ) : (
        <button
          onClick={copyToClipboard}
          className={`px-4 py-2 bg-transparent  text-primary rounded-lg hover:bg-primary/10 transition duration-300 ease-in-out flex items-center justify-center`}
        >
          {isCopied ? (
            <>
              <Check size={20} className="" />
            </>
          ) : (
            <>
              <Copy size={20} className="" />
            </>
          )}
        </button>
      )}
    </div>
  );
}
