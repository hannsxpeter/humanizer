#!/usr/bin/env node
'use strict';

// Copies the humanizer skill into Agent Skills folders so
// `npx @hxp-tools/humanizer` works. No dependencies, no network.

const fs = require('fs');
const os = require('os');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PKG = require('../package.json');
const SKILL = 'humanizer';
const PAYLOAD = ['SKILL.md', 'references', 'LICENSE'];

const TOOLS = {
  agents: { dir: '.agents', label: 'shared skills (Codex, Cursor, Gemini CLI, Copilot, OpenCode, Pi, Devin Desktop, Zed)' },
  claude: { dir: '.claude', label: 'Claude Code' },
  cline: { dir: '.cline', label: 'Cline' },
};

const COLORS = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
};

function c(color, text) {
  return process.stdout.isTTY ? COLORS[color] + text + COLORS.reset : text;
}

function usage() {
  console.log(`
${c('bold', 'humanizer')} ${c('dim', 'v' + PKG.version)}
Strip the tells. Keep the facts. Sound like you.

${c('bold', 'Usage')}
  npx @hxp-tools/humanizer
  npx @hxp-tools/humanizer --project
  npx @hxp-tools/humanizer --tools agents,claude,cline
  npx @hxp-tools/humanizer --uninstall
  npx @hxp-tools/humanizer --help

${c('bold', 'Targets')}
  agents   ~/.agents/skills/humanizer   always
  claude   ~/.claude/skills/humanizer   when ~/.claude exists
  cline    ~/.cline/skills/humanizer    when ~/.cline exists

  --project uses the current directory instead of your home directory.

${c('bold', 'After install')}
  Restart your coding agent, then ask it to humanize a draft.
`);
}

function parse(argv) {
  const opts = { project: false, uninstall: false, tools: null };
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg === '--project') opts.project = true;
    else if (arg === '--uninstall') opts.uninstall = true;
    else if (arg === '--help' || arg === '-h') opts.help = true;
    else if (arg === '--version' || arg === '-v') opts.version = true;
    else if (arg === '--tools' || arg.startsWith('--tools=')) {
      const value = arg.includes('=') ? arg.slice(arg.indexOf('=') + 1) : argv[++i];
      if (!value) throw new Error('--tools needs a list, for example --tools agents,claude');
      opts.tools = value.split(',').map((t) => t.trim()).filter(Boolean);
      const unknown = opts.tools.filter((t) => !TOOLS[t]);
      if (unknown.length) throw new Error(`unknown tool: ${unknown.join(', ')} (use ${Object.keys(TOOLS).join(', ')})`);
    } else throw new Error(`unknown option: ${arg}`);
  }
  return opts;
}

function pickTools(base, opts) {
  if (opts.tools) return opts.tools;
  return Object.keys(TOOLS).filter(
    (t) => t === 'agents' || fs.existsSync(path.join(base, TOOLS[t].dir))
  );
}

function isHumanizer(dest) {
  const skill = path.join(dest, 'SKILL.md');
  if (!fs.existsSync(skill)) return false;
  return /^name:\s*humanizer\s*$/m.test(fs.readFileSync(skill, 'utf8'));
}

function install(dest) {
  if (fs.existsSync(path.join(dest, '.git'))) {
    return ['skip', 'git clone; update it with git pull'];
  }
  const existed = fs.existsSync(dest);
  if (existed && !isHumanizer(dest)) {
    return ['skip', 'folder exists and is not humanizer; left alone'];
  }
  if (existed) fs.rmSync(dest, { recursive: true, force: true });
  fs.mkdirSync(dest, { recursive: true });
  for (const item of PAYLOAD) {
    fs.cpSync(path.join(ROOT, item), path.join(dest, item), { recursive: true });
  }
  return ['ok', existed ? 'updated' : 'installed'];
}

function uninstall(dest) {
  if (!fs.existsSync(dest)) return ['skip', 'not installed'];
  if (fs.existsSync(path.join(dest, '.git'))) return ['skip', 'git clone; remove it yourself'];
  if (!isHumanizer(dest)) return ['skip', 'not a humanizer install; left alone'];
  fs.rmSync(dest, { recursive: true, force: true });
  return ['ok', 'removed'];
}

function main(argv) {
  let opts;
  try {
    opts = parse(argv.slice(2));
  } catch (error) {
    console.error(c('red', error.message));
    return 2;
  }
  if (opts.help) {
    usage();
    return 0;
  }
  if (opts.version) {
    console.log(PKG.version);
    return 0;
  }

  const base = opts.project ? process.cwd() : os.homedir();
  const tools = pickTools(base, opts);
  console.log(c('cyan', 'humanizer') + ' ' + c('dim', 'v' + PKG.version));

  let ok = 0;
  for (const tool of tools) {
    const dest = path.join(base, TOOLS[tool].dir, 'skills', SKILL);
    let status;
    let note;
    try {
      [status, note] = opts.uninstall ? uninstall(dest) : install(dest);
    } catch (error) {
      [status, note] = ['fail', error.message];
    }
    if (status === 'ok') ok++;
    const color = status === 'ok' ? 'green' : status === 'skip' ? 'yellow' : 'red';
    console.log(`  ${c(color, note.padEnd(9))} ${dest} ${c('dim', TOOLS[tool].label)}`);
    if (status === 'fail') return 1;
  }

  if (!opts.uninstall && ok > 0) {
    console.log('');
    console.log(c('green', 'Press start: restart your agent, then ask it to humanize a draft.'));
    console.log(c('dim', 'Docs: ' + PKG.homepage));
  }
  return 0;
}

process.exitCode = main(process.argv);
