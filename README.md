# Gemini CLI Setup Guide

This guide provides a comprehensive walkthrough for setting up the Google Gemini Command-Line Interface (CLI), from checking prerequisites to installation and configuration.

## Table of Contents
1.  [Prerequisites: Node.js and npm](#prerequisites-nodejs-and-npm)
    * [Step 1: Check if Node.js and npm are Installed](#step-1-check-if-nodejs-and-npm-are-installed)
    * [Step 2: Install Node.js and npm if Needed](#step-2-install-nodejs-and-npm-if-needed)
2.  [Gemini CLI Installation & Configuration](#gemini-cli-installation--configuration)
    * [Step 1: Install the Gemini CLI Package](#step-1-install-the-gemini-cli-package)
    * [Step 2: Configure and Authenticate](#step-2-configure-and-authenticate)
3.  [Uninstallation Guide](#uninstallation-guide)

## Prerequisites: Node.js and npm

The Gemini CLI is distributed via `npm` (Node Package Manager), which is bundled with Node.js. It is essential to have a recent version of both to ensure compatibility.

### Step 1: Check if Node.js and npm are Installed

Open your terminal or command prompt and run the following commands to check if you have Node.js and npm installed.

To check your **Node.js** version (version 18 or higher is required):
```bash
node -v
````

*Example output: `v18.18.0`*

To check your **npm** version:

```bash
npm -v
```

*Example output: `9.8.1`*

If both commands return a valid version number that meets the requirements, you can proceed to the next section.

### Step 2: Install Node.js and npm if Needed

If the commands above result in an error like "command not found" or the version is too old, you need to install or update Node.js.

1.  **Go to the official Node.js website:** [https://nodejs.org/](https://nodejs.org/)
2.  **Download the installer:** Choose the **LTS (Long Term Support)** version, which is recommended for most users.
3.  **Run the installer:** Follow the on-screen instructions. The installer will automatically add both `node` and `npm` to your system's PATH.

After installation, close and reopen your terminal and run the `node -v` and `npm -v` commands again to verify that the installation was successful.

## Gemini CLI Installation & Configuration

With Node.js and npm ready, you can now install the Gemini CLI.

### Step 1: Install the Gemini CLI Package

Run the following command in your terminal to install the `@google/gemini-cli` package globally. The `-g` flag ensures the `gemini` command is accessible from any directory in your terminal.

```bash
npm install -g @google/gemini-cli
```

### Step 2: Configure and Authenticate

The first time you run the CLI, it will guide you through a one-time authentication process to connect with your Google account.

1.  **Start the Gemini CLI:**
    ```bash
    gemini
    ```
2.  **Authenticate:** The CLI will provide a URL. Copy and paste this URL into your web browser.
3.  **Grant Permissions:** Log in with your Google account and grant the necessary permissions when prompted.
4.  **Confirmation:** After successful authentication, you will see a confirmation page. You can now return to your terminal.

Your Gemini CLI is now configured and ready for use\!

## Uninstallation Guide

If you need to remove the Gemini CLI from your system, you can do so with a single command.

```bash
npm uninstall -g @google/gemini-cli
```

This command will remove the globally installed package. For a complete cleanup, you may also want to remove the configuration directory:

  * **macOS/Linux:** `rm -rf ~/.gemini`
  * **Windows:** Delete the `.gemini` folder from your user directory (`C:\Users\YourUsername`).
