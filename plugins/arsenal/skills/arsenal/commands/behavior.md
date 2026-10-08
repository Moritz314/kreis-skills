# behavior

## Purpose

Views, adds, edits and deletes the standing preference memory: one sentence per rule, dated, with its origin, no prose. This is what makes `behavior.md`'s preflight load meaningful everywhere else, a preference that only lives in one conversation is not a standing rule.

## Arguments

`behavior` (show the list)
`behavior add "<rule>" [project]`
`behavior edit <n> "<new text>"`
`behavior remove <n>`

`n` is the entry's position in the shown list, or a distinctive text fragment to match against.

## Preconditions (gates)

1. This command loads `behavior.md` from the sync path itself and is the one command allowed to create it if missing, rather than aborting. If it does not exist: create it with a short header comment and proceed.
2. No ARMOURY gate, this command is global.

## Procedure

1. **No argument:** read and display every entry in `behavior.md`, in date order.
2. **`add`:** append one line: `- YYYY-MM-DD [<project or "global">] <one sentence>.` Reject anything that isn't a single, direct sentence, ask for a tighter phrasing instead of storing prose.
3. **`edit`:** replace the matched entry's text in place, keep its original date, note the project origin unchanged unless told otherwise.
4. **`remove`:** delete the matched entry, confirm what was removed.
5. **Automatic entries (triggered from other commands, not run directly):** when `critics` or `build` sees the user reject or correct a suggestion, ask once, "save as a standing rule?" On yes, append an entry per step 2's format with the originating project noted. Never ask twice for the same rejection, and never add an entry without that explicit yes.

## Output

The current list on a bare call; a modified `behavior.md` on `add`/`edit`/`remove`.

## Abort conditions

None specific to reading or writing this file, it self-heals when missing. `edit`/`remove` with no matching entry: report that plainly and show the current list instead of guessing which entry was meant.

## References

None. `behavior.md`'s format is defined here and consumed as a preflight load by every other command.
