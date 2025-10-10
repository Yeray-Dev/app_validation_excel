from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
import pandas as pd

def render_aggrid(
        df,
        editable_columns = None,
        hidden_columns = None,
        height = 400,
        pagination = True,
        single_click_edit = True
):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        editable = False,
        resizable = True,
        filter = True,
        sortable = True,
        wrapText = True,
        autoHeight = True
    )

    if pagination:
        gb.configure_pagination(paginationAutoPageSize=True)
    
    if editable_columns:
        for col in editable_columns:
            if col in df.columns:
                if pd.api.types.is_bool_dtype(df[col]):
                    gb.configure_column(
                        col,
                        editable=True,
                        cellRenderer="agCheckboxCellRenderer",
                        cellEditor="agCheckboxCellEditor"
                    )
                else:
                    gb.configure_column(col, editable=True)

    if hidden_columns:
        for col in hidden_columns:
            if col in df.columns:
                gb.configure_column(col, hide = True)

    grid_options = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions = grid_options,
        height = height,
        update_mode = GridUpdateMode.VALUE_CHANGED,
        allow_unsafe_jscode = True 
    )
    return grid_response