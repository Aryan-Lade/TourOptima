# DLiquid Landing - Hydra Bittensor Liquidity Subnet

A Next.js website for Subnet 66 - Alpha bandwidth rights direct liquidity across Bittensor subnets through miner competition.

## Fixed Issues

✅ **Missing package.json** - Created with all required dependencies
✅ **Missing next.config.js** - Added Next.js configuration
✅ **Missing tailwind.config.ts** - Added Tailwind CSS configuration with custom animations
✅ **Missing tsconfig.json** - Added TypeScript configuration
✅ **Missing postcss.config.js** - Added PostCSS configuration
✅ **Missing dependencies** - Added recharts, @radix-ui/react-slot, @radix-ui/react-dialog
✅ **Missing lib/utils.ts** - Created utility functions for className merging
✅ **Missing next-env.d.ts** - Added Next.js environment types

## Getting Started

### Prerequisites
- Node.js 18+ or Bun
- npm, yarn, or bun package manager

### Installation

```bash
# Install dependencies
npm install
# or
yarn install
# or
bun install
```

### Development

```bash
# Start development server
npm run dev
# or
yarn dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) to view the website.

### Build

```bash
# Build for production
npm run build
# or
yarn build
# or
bun build
```

### Start Production Server

```bash
# Start production server
npm start
# or
yarn start
# or
bun start
```

## Features

- 🎨 Modern UI with Tailwind CSS and shadcn/ui components
- 📱 Responsive design
- 🌙 Dark theme with blue color scheme
- ✨ Animated background with blob effects
- 📊 Dashboard with charts (using Recharts)
- 📄 Whitepaper section
- 🗳️ Voting modal functionality
- 🔧 TypeScript for type safety
- 🎯 Biome for linting and formatting

## Project Structure

```
src/
├── app/
│   ├── globals.css          # Global styles
│   ├── layout.tsx           # Root layout
│   ├── page.tsx             # Home page
│   ├── ClientBody.tsx       # Client-side body wrapper
│   └── test-whitepaper/     # Test whitepaper page
├── components/
│   ├── ui/                  # shadcn/ui components
│   ├── Dashboard.tsx        # Dashboard component
│   ├── SubnetDetails.tsx    # Subnet details component
│   ├── VoteModal.tsx        # Voting modal component
│   └── Whitepaper.tsx       # Whitepaper component
└── lib/
    └── utils.ts             # Utility functions
```

## Technologies Used

- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **shadcn/ui** - UI components
- **Recharts** - Charts and data visualization
- **Radix UI** - Headless UI components
- **Lucide React** - Icons
- **Biome** - Linting and formatting

## License

This project is private and proprietary.
