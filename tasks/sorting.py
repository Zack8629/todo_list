def sorting_tasks(**kwargs):
    sorting = kwargs.get('sorting')
    field = kwargs.get('field')
    if sorting:
        sorting = sorting[0]
        field = field[0]
        if sorting == 'asc':
            sorting_direction = ''
        else:
            sorting_direction = '-'

        return sorting_direction + field
