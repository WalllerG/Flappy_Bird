# Plan: Convert Flappy Bird from Pygame to Web (Phaser.js + Node.js)

## Context
The user has a working pygame Flappy Bird game (game.py) and wants to convert it to a web-based game that anyone can play. The goal is to create a modern, smooth-running web game with a decent UI, using Phaser.js for the game engine and Node.js/Express for the web server.

## Current State Analysis

**Existing Assets:**
- `game.py` - Pygame implementation with core game logic
- `images/` - background.png, bird.png, tunnel1.png, tunnel2.png
- `game_font.ttf`, `score_font.ttf` - Custom fonts
- Game mechanics: gravity, jumping, tunnel generation, collision detection, scoring

**Game Logic to Port:**
- Bird with physics (gravity = 0.2, jump_strength = -3.5)
- 4 tunnels moving left at 4 pixels/frame
- Gap size = 130px, gap Y randomized between 200-400
- Score increments when bird passes tunnel (x < 110)
- Collision with ground (y >= 620) or tunnels = game over
- Game over screen with restart button

## Implementation Strategy

### Phase 1: Project Setup
**Files to create:**
- `package.json` - Dependencies (express, phaser)
- `server.js` - Express server to serve static files and handle high scores API
- `public/` - Frontend static files
  - `index.html` - Main HTML structure
  - `css/styles.css` - Modern UI styling
  - `js/game.js` - Phaser game scenes
  - `assets/` - Copied images and fonts

### Phase 2: HTML Structure
- Single-page application with Phaser canvas
- Modern landing page design with:
  - Game title (large, styled)
  - Instructions
  - Play button
  - High score display
  - Responsive layout
- Game canvas centered on page
- Phaser will handle in-game UI (score, game over screen)

### Phase 3: Phaser Game Implementation

**Scene Structure:**
1. `BootScene` - Preload all assets (images, fonts, sounds)
2. `MenuScene` - Landing page with title and Play button
3. `GameScene` - Main gameplay
   - Create bird sprite with physics (arcade physics)
   - Create tunnel group with 4 tunnels
   - Implement bird jump on input (space, click, touch)
   - Move tunnels left continuously
   - Collision detection (bird vs ground vs tunnels)
   - Score tracking and display
   - Generate new tunnels when old ones exit screen
4. `GameOverScene` - Show final score, high score, restart button

**Key Technical Details:**
- Use Phaser's Arcade Physics for gravity and collisions
- Load custom fonts using Phaser's font loader
- Bird physics: velocity.y += gravity, jump sets velocity.y = jump_strength
- Tunnel collision: use separate physics bodies for top and bottom tunnels
- Ground collision: use a static ground body
- Score zone: invisible trigger at x=110 that increments score
- High scores: store in localStorage (no backend needed) with fallback

**Controls:**
- Keyboard: SPACE key
- Mouse: Click/tap anywhere
- Touch: Tap anywhere
- All mapped to same jump action

### Phase 4: Audio Implementation
- Generate or add sound effects:
  - `jump.wav` - Bird flap sound
  - `score.wav` - Point scoring
  - `hit.wav` - Collision/game over
  - `wing.wav` (optional) - Continuous flapping ambiance
- Preload in BootScene
- Play on appropriate events

### Phase 5: Modern UI & Styling

**CSS Design:**
- Modern gradient backgrounds
- Card-based layout with shadows
- Smooth transitions/animations
- Responsive design (flexbox/grid)
- Mobile-friendly viewport
- Typography: Use custom fonts or Google Fonts as fallback

**Color Scheme (suggested):**
- Primary: Sky blue gradient (#87CEEB to #E0F6FF)
- Accent: Orange/yellow (#F5A623) for buttons and highlights
- Text: White with shadows for readability
- Dark overlay for game over modal

### Phase 6: High Score Tracking
- Use localStorage to persist best score
- Initialize from localStorage on game start
- Update when new score exceeds previous high score
- Display on menu and game over screens
- No backend needed (simpler and works offline)

### Phase 7: Mobile Optimization
- Responsive canvas that scales to viewport
- Touch event support (Phaser handles this automatically)
- Prevent default touch behaviors to avoid page scrolling
- Proper viewport meta tag for mobile

### Phase 8: Testing & Polish
- Test on different screen sizes
- Verify all game mechanics match original
- Check collision detection accuracy
- Ensure smooth 60 FPS performance
- Test touch/click/keyboard controls

## Files to Create/Modify

### New Files:
1. `package.json`
2. `server.js`
3. `public/index.html`
4. `public/css/styles.css`
5. `public/js/game.js`
6. `public/assets/` (copy images & fonts here)
7. `.gitignore`

### Existing Files (to copy):
- `images/*.png` → `public/assets/`
- `*.ttf` → `public/assets/`

## Verification Steps

1. **Installation:**
   - Run `npm install`
   - Verify dependencies install correctly

2. **Server Startup:**
   - Run `node server.js` or `npm start`
   - Server should start on port 3000
   - Access http://localhost:3000

3. **Game Functionality:**
   - Landing page loads with styled UI
   - Click "Play" starts game
   - Bird responds to space/click/touch
   - Tunnels scroll smoothly
   - Score increments correctly
   - Collision triggers game over
   - Restart button works
   - High score persists across sessions

4. **Audio:**
   - Jump sound plays on flap
   - Score sound plays when passing tunnel
   - Hit sound plays on collision

5. **Responsive Design:**
   - Resize browser window
   - Game canvas centers properly
   - Controls work on mobile (use device or emulator)

## Technical Stack
- **Frontend:** Phaser 3.60+ (latest stable)
- **Backend:** Express.js (minimal, only for serving static files)
- **Package Manager:** npm
- **Assets:** Reuse existing PNGs and TTF fonts

## Notes
- The game canvas size: 800x600 (maintain original aspect ratio)
- All game assets remain the same for visual consistency
- No game logic changes - exact recreation of original mechanics
- Modern UI only affects surrounding page, not in-game graphics
- High score tracking uses browser localStorage (no server database)
