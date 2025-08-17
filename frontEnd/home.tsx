import React, { useState } from 'react';

const Home: React.FC = () => {
    const [youtubeUrl, setYoutubeUrl] = useState('');

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setYoutubeUrl(e.target.value);
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Handle the submitted YouTube URL here
        alert(`Submitted URL: ${youtubeUrl}`);
    };

    return (
        <div style={{ maxWidth: 500, margin: '2rem auto', padding: '2rem', border: '1px solid #ddd', borderRadius: 8 }}>
            <h1>Bienvenue!</h1>
            <p>
                Welcome to the French Listening Test Generator website.<br />
                Please enter a YouTube URL to get started.
            </p>
            <form onSubmit={handleSubmit}>
                <input
                    type="url"
                    placeholder="Enter YouTube URL"
                    value={youtubeUrl}
                    onChange={handleInputChange}
                    style={{ width: '100%', padding: '0.5rem', marginBottom: '1rem' }}
                    required
                />
                <button type="submit" style={{ padding: '0.5rem 1rem' }}>
                    Submit
                </button>
            </form>
        </div>
    );
};

export default Home;