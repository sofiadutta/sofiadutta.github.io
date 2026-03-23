## 2026-03-23 - Iframe Sandbox Restrictions
**Vulnerability:** Missing sandbox restrictions on third-party iframes (YouTube).
**Learning:** Iframes without a sandbox attribute can execute scripts, navigate the top-level window, or submit forms, posing a significant risk if the third-party content is compromised.
**Prevention:** Always apply a restrictive `sandbox` attribute (e.g., `allow-scripts allow-same-origin allow-presentation allow-popups`) when embedding third-party iframes to enforce defense-in-depth.
