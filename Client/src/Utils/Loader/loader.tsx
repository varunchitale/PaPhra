import * as React from 'react';

export function Loader() {
    return (
        <div style={{ marginTop: '40px', textAlign: 'center' }}>
            <img src="/static_images/filter-loading.gif" width="70" height="70" />
        </div>
    );
}