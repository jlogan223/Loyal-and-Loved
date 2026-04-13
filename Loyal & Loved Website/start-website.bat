@echo off
REM Loyal & Loved UK — Local Development Server
REM Starts a simple HTTP server on port 3005

setlocal enabledelayedexpansion

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Check if npm is installed
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: npm is not installed
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

REM Create a simple server script if it doesn't exist
if not exist "server.js" (
    echo Creating local development server...
    (
        echo const http = require('http');
        echo const fs = require('fs');
        echo const path = require('path');
        echo.
        echo const PORT = 3005;
        echo.
        echo const server = http.createServer((req, res) =^> {
        echo   let filePath = path.join(__dirname, req.url);
        echo.
        echo   // Default to index.html for root
        echo   if (filePath === path.join(__dirname, '/') || req.url === '/') {
        echo     filePath = path.join(__dirname, 'index.html');
        echo   }
        echo.
        echo   // Try with .html extension if no extension given
        echo   if (!path.extname(filePath)) {
        echo     filePath += '.html';
        echo   }
        echo.
        echo   fs.readFile(filePath, (err, data) =^> {
        echo     if (err) {
        echo       res.writeHead(404, { 'Content-Type': 'text/html' });
        echo       res.end('^<h1^>404 - File Not Found^</h1^>');
        echo       return;
        echo     }
        echo.
        echo     // Determine content type
        echo     const ext = path.extname(filePath);
        echo     let contentType = 'text/html';
        echo     if (ext === '.css') contentType = 'text/css';
        echo     else if (ext === '.js') contentType = 'text/javascript';
        echo     else if (ext === '.json') contentType = 'application/json';
        echo     else if (ext === '.xml') contentType = 'text/xml';
        echo     else if (ext === '.png') contentType = 'image/png';
        echo     else if (ext === '.jpg' ^| ext === '.jpeg') contentType = 'image/jpeg';
        echo     else if (ext === '.gif') contentType = 'image/gif';
        echo.
        echo     res.writeHead(200, { 'Content-Type': contentType });
        echo     res.end(data);
        echo   });
        echo });
        echo.
        echo server.listen(PORT, '127.0.0.1', () =^> {
        echo   console.log('Loyal ^&amp; Loved UK - Local Development Server');
        echo   console.log(`Server is running at http://127.0.0.1:${PORT}`);
        echo   console.log('Press Ctrl+C to stop the server');
        echo });
    ) > server.js
)

REM Start the server
echo.
echo Starting Loyal ^& Loved UK development server on port 3005...
echo Open your browser to http://127.0.0.1:3005
echo.
echo Press Ctrl+C to stop the server
echo.

node server.js

pause
