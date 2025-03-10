/*
-------------------------------------------------------------------------
* Template Name    : Sliced Pro - Tailwind CSS Admin & Dashboard Template   * 
* Author           : SRBThemes                                              *
* Version          : 1.0.0                                                  *
* Created          : October 2024                                           *
* File Description : form-editor init Js File                               *
*------------------------------------------------------------------------
*/

function app() {
    return {
        sliced: null,
        init: function (el) {
            // Get el
            this.sliced = el;
            // Add CSS
            if (this.sliced) {
                this.sliced.contentDocument.querySelector(
                    "head"
                ).innerHTML += `<style>
            *, ::after, ::before {box-sizing: border-box;}
            :root {tab-size: 4;}
            html {line-height: 1;text-size-adjust: 100%;}
            body {margin: 0px; padding: 1rem 0.5rem;}
            body {font-family: Outfit Sans;}
            p {margin: 0px;line-height:1.2;}
            </style>`;
                this.sliced.contentDocument.body.innerHTML += `
            <h1>Hello World!</h1>
            <p>Welcome to the pure AlpineJS and Tailwind sliced.</p>
            `;
                // Make editable
                this.sliced.contentDocument.designMode = "on";
            }
        },
        format: function (cmd, param) {
            if (this.sliced) {
                this.sliced.contentDocument.execCommand(cmd, !1, param || null);
            }
        },
    };
}
