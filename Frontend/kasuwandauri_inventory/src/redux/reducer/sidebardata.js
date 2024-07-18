import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchSidebar = createAsyncThunk('data/fetchSidebar', async () => {
    const response = await axios.get('http://localhost:8000/api/sidebar/');
    return response.data.data;
});

const sidebarSlice = createSlice({
    name: 'data',
    initialState: {
        items: [],
        status: 'idle',
        error: null,
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchSidebar.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(fetchSidebar.fulfilled, (state, action) => {
                state.status = 'success';
                state.items = action.payload;
            })
            .addCase(fetchSidebar.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
            });
    },
});

export default sidebarSlice.reducer;
